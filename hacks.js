var s = new WebSocket("ws://127.0.0.1:8002");

s.addEventListener("message", (event) => {

  var before = parseInt(document.querySelector("#stats > div:nth-child(2) > p").innerText);

  var n   = event.data.trim();
  var str = '[aria-label="rotate tile no. ' + n + ' clockwise"]';
  var elt = document.querySelector(str);

  if (elt) {
    // Elt might be gone if we kept clicking after we won.
    elt.click()
  }

  function f () {
    var after = parseInt(document.querySelector("#stats > div:nth-child(2) > p").innerText);
    // Good: Send 1 and n
    if (after < before) {
      s.send("1," + n);
    }

    // Good: Send 0 and n
    if (after > before) {
      s.send("0," + n);
    }
  }
  // We need to wait a moment for the score to be updated.
  setTimeout(f, 200);
});
