import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Which city you want to analyze :").lower()
    cities = ['chicago', 'new york city', 'washington']
    
    while city in cities or city in cities:
        break
    while city not in cities:
        print("Please enter a choice form the following cities chicago, new york city or washington")
        city = input("Which city you want to analyze? ").lower()
        continue
        
    
    

    # TO DO: get user input for month (all, january, february, ... , june)
    global months
    global days
    global day
    global month
    
    months = ['all','january','febuary','march','april','may','june']
    while True:
        month = input("Select a month from {}, {}, {}, {}, {}, {} or {}:".format(*months)).strip().lower()
        if month in months:
            break
        
    #month =months.index(month)+1
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("please choose a day from the following list('monday','tuesday','wednesday','thursday','friday','saturday','sunday')to analyze or use all to see the whole week :").lower()
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while day.lower() in days:
        break
    while day not in days:
        print("Please enter a valid choice !")
        day=input("please choose a day from the following list('monday','tuesday','wednesday','thursday','friday','saturday','sunday')to analyze or use all to see the whole week :").lower()
        continue
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    city=pd.read_csv(CITY_DATA[city])
    df=pd.DataFrame(city)
    df['month']=pd.to_datetime(df['Start Time']).dt.month
    df['day']=pd.to_datetime(df['Start Time']).dt.day_name()
    if month != 'all':
        df = df[df['month'] == months.index(month)]
        
    if day!='all':
        df = df[df['day'] == day.title()]

    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month!='all':
        popular_month=df['month'].mode()[0]
        print('The most common month is {}.'.format(popular_month))

    # TO DO: display the most common day of week
    try:
        popular_day =df['day'].mode()[0]
        print('The most common day of week is {}.'.format(popular_day))
    except Exception as e:
        print(e)

    # TO DO: display the most common start hour

    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The rush hour is {}.'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('The most commonly used start station is {}.'.format(popular_start_station))


    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('The most commonly used end station is {}.'.format(popular_end_station))
    

    # TO DO: display most frequent combination of start station and end station trip
    popular_station=(df['Start Station']+' and also '+df['End Station']).mode()[0]
    print('The popular station is {}.'.format(popular_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The sum of trip duration is {}.'.format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The mean of Trip Duration is {}.'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types=df['User Type'].value_counts()
    print('Our customers types are {}.' .format(counts_of_user_types))


    # TO DO: Display counts of gender
    try:
        counts_of_gender=df['Gender'].value_counts()
        print('Our customers gender are {}.'.format(counts_of_gender))
    except Exception as e:
        print("Washington deosn't have gender data ")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        yongest_coustomer_birthday_year=df['Birth Year'].max()
        print('Our youngest customer birthyear is {}.'.format(yongest_coustomer_birthday_year))
    except Exception as e:
        print("Washington doesn't have birth day data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    i = 0
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            raw_data = input('\nDo you want to see five raw data.\n')
            print(df.iloc[i:i+5])
            i +=5
            if raw_data !='yes':    
                break
        
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
