# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAYS;"
user_table_drop = "DROP TABLE IF EXISTS USERS;"
song_table_drop = "DROP TABLE IF EXISTS SONGS;"
artist_table_drop = "DROP TABLE IF EXISTS ARTISTS;"
time_table_drop = "DROP TABLE IF EXISTS TIME;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE SONGPLAYS (
        SONGPLAY_ID SERIAL PRIMARY KEY
       , START_TIME TIME NOT NULL
       , USER_ID NUMERIC(3) NOT NULL
       , LEVEL VARCHAR(4) NOT NULL
       , SONG_ID VARCHAR(20)
       , ARTIST_ID VARCHAR(20)
       , SESSION_ID VARCHAR(4) NOT NULL
       , LOCATION VARCHAR(100) NOT NULL
       , USER_AGENT VARCHAR(150) NOT NULL
    );
""")

user_table_create = ("""
    CREATE TABLE USERS (
          USER_ID NUMERIC(3) PRIMARY KEY
        , FIRST_NAME VARCHAR(15)
        , LAST_NAME VARCHAR(15)
        , GENDER VARCHAR(1)
        , LEVEL VARCHAR(4) NOT NULL
    );
""")

song_table_create = ("""
    CREATE TABLE SONGS (
          SONG_ID VARCHAR(20) PRIMARY KEY
        , TITLE VARCHAR(100)
        , ARTIST_ID VARCHAR(20)
        , YEAR NUMERIC(4, 0)
        , DURATION NUMERIC NOT NULL
    );
""")

artist_table_create = ("""
    CREATE TABLE ARTISTS (
          ARTIST_ID VARCHAR(20) PRIMARY KEY
        , NAME VARCHAR(100) NOT NULL
        , LOCATION VARCHAR(100)
        , LATITUDE NUMERIC(7)
        , LONGITUDE NUMERIC(7)
    );
""")

time_table_create = ("""
    CREATE TABLE TIME (
          START_TIME TIME PRIMARY KEY
        , HOUR NUMERIC(2) NOT NULL
        , DAY NUMERIC(2) NOT NULL
        , WEEK NUMERIC(2) NOT NULL
        , MONTH NUMERIC(2) NOT NULL
        , YEAR NUMERIC(4) NOT NULL
        , WEEKDAY NUMERIC(1) NOT NULL
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO SONGPLAYS (
       START_TIME
       , USER_ID
       , LEVEL
       , SONG_ID
       , ARTIST_ID
       , SESSION_ID
       , LOCATION
       , USER_AGENT
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    INSERT INTO USERS (
          USER_ID
        , FIRST_NAME
        , LAST_NAME
        , GENDER
        , LEVEL
    )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (USER_ID)
    DO 
        UPDATE SET 
            LEVEL = EXCLUDED.LEVEL;
""")

song_table_insert = ("""
    INSERT INTO SONGS (
          SONG_ID
        , TITLE
        , ARTIST_ID
        , YEAR
        , DURATION ) 
    VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
    INSERT INTO ARTISTS (
          ARTIST_ID
        , NAME
        , LOCATION
        , LATITUDE
        , LONGITUDE
    )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (ARTIST_ID)
    DO NOTHING;
    ;
""")


time_table_insert = ("""
    INSERT INTO TIME (
        START_TIME
        , HOUR
        , DAY
        , WEEK
        , MONTH
        , YEAR
        , WEEKDAY
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (START_TIME)
    DO
        NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT SONGS.SONG_ID, ARTISTS.ARTIST_ID
    FROM SONGS
        LEFT JOIN ARTISTS ON SONGS.ARTIST_ID = ARTISTS.ARTIST_ID
    WHERE
        SONGS.TITLE = %s
        AND ARTISTS.NAME = %s
        AND SONGS.DURATION = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]