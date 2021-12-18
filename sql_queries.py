# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplay"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplay
(
    songplay_id SERIAL primary key, 
    start_time bigint NOT NULL, 
    user_id int NOT NULL,
    level varchar,
    song_id varchar, 
    artist_id varchar, 
    session_id varchar, 
    location varchar,
    user_agent varchar
)
""")

user_table_create = (""" CREATE TABLE IF NOT EXISTS users
(
    user_id int primary key,
    first_name varchar NOT NULL,
    last_name varchar NOT NULL, 
    gender varchar, 
    level varchar
)
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs
(
    song_id varchar primary key,
    title varchar NOT NULL,
    artist_id varchar NOT NULL,
    year int NOT NULL,
    duration numeric NOT NULL
)
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists
(
    artist_id varchar primary key,
    name varchar NOT NULL, 
    location varchar, 
    latitude numeric,
    longitude numeric
)
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time
(
    start_time bigint primary key, 
    hour int NOT NULL,
    day int NOT NULL, 
    week int NOT NULL,
    month int NOT NULL,
    year int NOT NULL, 
    weekday int NOT NULL
)
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplay 
(
    start_time, 
    user_id, 
    level,
    song_id, 
    artist_id,
    session_id, 
    location,
    user_agent
)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = (""" INSERT INTO users 
(
    user_id, 
    first_name,
    last_name,
    gender, 
    level
)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
    DO UPDATE SET level=EXCLUDED.level;
""")

song_table_insert = (""" INSERT INTO songs 
(
    song_id, 
    title, 
    artist_id,
    year,
    duration
)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id)
    DO NOTHING;
""")

artist_table_insert = (""" INSERT INTO artists 
(
    artist_id,
    name,
    location,
    latitude,
    longitude
)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id)
    DO NOTHING;
""")


time_table_insert = (""" INSERT INTO time 
(
    start_time,
    hour,
    day, 
    week,
    month,
    year, 
    weekday
)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time)
    DO NOTHING;
""")

# FIND SONGS

song_select = (""" SELECT songs.song_id, songs.artist_id FROM
    songs JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]