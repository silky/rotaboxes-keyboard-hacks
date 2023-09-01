# [Rotaboxes](https://rotaboxes.com/) hacks

Some terrible code to play [rotaboxes](https://rotaboxes.com/) via an external keyboard.


### QMK Stuff

1. Grab my branch of [`qmk_firmware`](https://github.com/silky/qmk_firmware/tree/rotaboxes-hacks)
1. To use the QMK code, you need the [SpiderIsland 5x5
   keyboard](https://www.aliexpress.com/item/1005002669909038.html)
1. Open the nix shell with `nix-shell` (wait patiently if it's your first
   time).
1. Run `qmk flash -kb winry/winry25tc -km programmable`


### Usage

1. Open [rotaboxes](https://rotaboxes.com/) and paste in the
   [hacks.js](./hacks.js) code into the browser console.
1. Run `./relay-server.py`
1. Press any button (aside from the bottom-left) to and watch the boxes
   rotate!


### Notes

- For reasons I don't quite understand, I couldn't get the so-called
["progammable"
keys](https://github.com/qmk/qmk_firmware/blob/master/docs/keycodes.md#programmable-button-support-idprogrammable-button) to come through to linux, which is unfortunate. So I opted to make the keyboard send `[a .. y]` keys instead.
- Hence, you need to focus somewhere where it's okay to be writing those
letters.
- Rotaboxes, in it's infinite wisdom, hides the HTML element I depend on if
your screen is too small (responsive website!); so you need to make sure the
screen is wide enough when you paste in the JavaScript hacks (!)
- It doesn't sync with the present-state of the game; but it should turn on
and off as you get tiles "correct".


### Demo

<iframe src="https://player.vimeo.com/video/860187767?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" title="rotaboxes hacks"></iframe>


### Todo

- [ ] I think the Python async code might be terrible and need a cleanup
- [ ] It doesn't handle errors very well
- [ ] Make it use the programmable buttons by investigating libevdev or otherwise


