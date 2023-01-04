DROP TABLE IF EXISTS tracks;

CREATE TABLE tracks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    genre TEXT NOT NULL,
    length INTEGER NOT NULL
);

INSERT INTO tracks (id, title, artist, genre, length) VALUES
    (1, 'Bohemian Rhapsody', 'Queen', 'Rock', 600),
    (2, 'Stairway to Heaven', 'Led Zeppelin', 'Rock', 480),
    (3, 'Sweet Child o'' Mine', 'Guns N'' Roses', 'Rock', 360),
    (4, 'Hotel California', 'Eagles', 'Rock', 480),
    (5, 'Imagine', 'John Lennon', 'Pop', 300),
    (6, 'Thinking Out Loud', 'Ed Sheeran', 'Pop', 240),
    (7, 'Shape of You', 'Ed Sheeran', 'Pop', 180),
    (8, 'Don''t Stop Believin''', 'Journey', 'Rock', 240),
    (9, 'Billie Jean', 'Michael Jackson', 'Pop', 300),
    (10, 'Smooth', 'Santana ft. Rob Thomas', 'Rock', 240);