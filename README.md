# spoticard
spotify lyrics card creator

# samples
![example 1](output.png)
![example 2](output1.png)

# how to use, help and usage
```
   Usage:
 ./spoticard TRACK_ID "LYRICS" TIMESTAMP ... ...
 Example: ./spoticard 61dXty0FR61qyVczdM49F4 "Winner, God know I'm a winner, When she pull up on me I be in her, I'ma eat out shawty like a dinner, Money comin' in it's like a printer, If she leaving shawty getting thinner
I'm like who got the keys? For real, Who got the keys? Yeah for real, I'm like who got the keys to the— uh, yeah, Who got the keys to the Bimmer?
Shawty she just a beginner huh, She look like Brittany no Renner huh" 1:40

Arguments and how to use them: (* = required)
 *  track_id: the id of the song
 *    lyrics: lyrics of the song. i suggest to format it to look good, for example
              breaking lines or adding newlines when there is supposed to be a newline
 * timestamp: the timestamp of the lyrics

   lyrics_brightness: how bright the lyrics text should be, 4th argument. default:    1
    brightness_value: the backgrounds image brightness.                   default: 0.50
     roundness_value: how rounded the corners should be.                  default:   30
      blurness_value: how blurredd the background image should be.        default:    7
         normal_font: the size of artist and title.                       default:   44
          small_font:             lyrics and timestamp.                   default:   36
```

# requirements
PIL, requests, python-dotenv and numpy
```sh
pip install -r requirements
```

# setup
first,
```sh
git clone https://github.com/devlocalhost/spoticard
```

create a application in [spotify dashboard](https://developer.spotify.com/dashboard/applications), copy the client id and secret, create a .env file and
```
CLIENT_ID="YOUR_CLIENT_ID"
CLIENT_SECRET="YOUR_CLIENT_SECRET"
TOKEN=""
```

paste this, and of course, replace your client id and secret with the ones you got from the application you made. run the gettoken.py file, copy the output and put it in the 3rd line of the .env file (inside the quotes of TOKEN)

and thats it. try `./spoticard 61dXty0FR61qyVczdM49F4 "Winner, God know I'm a winner, When she pull up on me I be in her, I'ma eat out shawty like a dinner, Money comin' in it's like a printer, If she leaving shawty getting thinner
I'm like who got the keys? For real, Who got the keys? Yeah for real, I'm like who got the keys to the— uh, yeah, Who got the keys to the Bimmer?
Shawty she just a beginner huh, She look like Brittany no Renner huh" 1:40` as an example. a `output.png` file will be created

# other
want to contribute? found an issue/bug? feel free to open an issue/pr
