document.addEventListener('DOMContentLoaded', function() {
    var msg = document.getElementById('msg'),
        canvas = document.getElementsByTagName('canvas')[0],
        ctx = canvas.getContext('2d');

    canvas.addEventListener('click', function (e) {
        msg.style.display = 'none';
        ctx.beginPath();
        ctx.arc(e.clientX, e.clientY, 15+Math.random()*35, 0, Math.PI * 2, true);
        ctx.fillStyle = 'red';
        ctx.fill();
    });

    scaleCanvas();
    window.addEventListener('resize', scaleCanvas);

    function scaleCanvas() {
        canvas.width = canvas.clientWidth;
        canvas.height = canvas.clientHeight;
    }
});