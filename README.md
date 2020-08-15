# rifflink
`rifflink` painlessly symlinks RiffTrax-enhanced movies into your RiffTrax TV show directory, potentially saving you hours of time and hundreds of gigabytes of storage space.

For example, let's say you have the following directory structure:

```
Movies/
    Alien (1979)/
        Alien (1979).mkv
    Back to the Future (1985)/
        Back to the Future (1985).mkv
    Carnival of Souls (1962)/
        Carnival of Souls (1962).mkv
TV/
    RiffTrax/
```

You can run

```sh
rifflink.py Movies/ TV/RiffTrax/
```

and end up with something like

```
Movies/
    Alien (1979)/
        Alien (1979).mkv
    Back to the Future (1985)/
        Back to the Future (1985).mkv
    Carnival of Souls (1962)/
        Carnival of Souls (1962).mkv
TV/
    RiffTrax/
        1x80 - Carnival of Souls Three Riffer Edition.mkv@
        2x07 - Alien.mkv@
```

### requirements

One or more movies that:
- have a correct themoviedb filename in the form "Movie Name (Year).ext"
- contain at least one audio track with a label in which the word "riff" appears

### limitations
- only handles RiffTrax seasons 1 and 2
- only handles movie riffs, not tv episode riffs
- can't create multiple symlinks for movies that contain more than one RiffTrax, e.g. "Mike Solo" and "Three Riffer" 
- no customization of output season/episode numbering format

These will be addressed in a future update.