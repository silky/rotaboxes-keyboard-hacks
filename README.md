# [Rotaboxes](https://rotaboxes.com/) hacks

Some terrible code to play [rotaboxes](https://rotaboxes.com/) via an external keyboard.


### QMK Stuff

1. Grab my branch of [`qmk_firmware`](https://github.com/silky/qmk_firmware/tree/rotaboxes-hacks)
1. To use the QMK code, you need the [SpiderIsland 5x5
   keyboard](https://www.aliexpress.com/item/1005002669909038.html)
1. Open the nix shell with `nix-shell` (wait patiently if it's your first
   time).
1. Run `qmk flash -kb winry/winry25tc -km programmable`


### Requirements/development

Use [Nix flakes](https://nixos.wiki/wiki/Flakes) and `nix develop` or
[direnv](https://github.com/nix-community/nix-direnv).


### Usage

1. Run `./relay-server.py`
1. Open [rotaboxes](https://rotaboxes.com/) and paste in the
   [hacks.js](./hacks.js) code into the browser console.
1. Press any button (aside from the bottom-right) to and watch the boxes
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

[Video on vimeo](https://vimeo.com/860187767?share=copy)



### Todo

- [ ] I think the Python async code might be terrible and need a cleanup
- [ ] It doesn't handle errors very well
- [ ] Make it use the programmable buttons by investigating libevdev or otherwise
- [ ] Because there is one spare key, this could be made into the 'shift' key,
    and allow for rotation in the counter-clockwise direction, if one wished.
- [ ] Maybe come up with a nice map of the 6x4 board onto the 5x5 board; the
   present one doesn't do anything sensible.



