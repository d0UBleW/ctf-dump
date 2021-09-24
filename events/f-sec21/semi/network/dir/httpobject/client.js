document.addEventListener("DOMContentLoaded", function() {
    function x() {
        return Math.floor(100 * Math.random()) + 1
    }
    var n = {
            click: !1,
            move: !1,
            pos: {
                x: 0,
                y: 0
            },
            pos_prev: !1
        },
        e = document.getElementById("board"),
        t = e.getContext("2d"),
        i = window.innerWidth,
        c = window.innerHeight,
        r = io.connect();
    e.width = i, e.height = c, e.onmousedown = function(o) {
            n.click = !0
        }, e.onmouseup = function(o) {
            n.click = !1
        }, e.onmousemove = function(e) {
            n.pos.x = e.clientX / i + x(), n.pos.y = e.clientY / c + x(), n.move = !0
        }, r.on("coor", function(o) {
            var n = o.line,
                x1 = (n[0].x - Math.floor(n[0].x)) * i,
                y1 = (n[0].y - Math.floor(n[0].y)) * c,
                x2 = (n[1].x - Math.floor(n[1].x)) * i,
                y2 = (n[1].y - Math.floor(n[1].y)) * c;
            t.beginPath(), t.moveTo(x1, y1), t.lineTo(x2, y2), t.stroke()
        }),
        function o() {
            n.click && n.move && n.pos_prev && (r.emit("coor", {
                line: [n.pos, n.pos_prev]
            }), n.move = !1), n.pos_prev = {
                x: n.pos.x,
                y: n.pos.y
            }, setTimeout(o, 25)
        }()
});