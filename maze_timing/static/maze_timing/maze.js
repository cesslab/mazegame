const CANVAS = document.getElementById("mazecanvas");
const CONTEXT = CANVAS.getContext("2d");

const RED_ID = 0;
const GREEN_ID = 1;
const BLUE_ID = 2;

const BLUE = "#0000FF";
const GREEN = "#00FF00";
const WHITE = "#FFFFFF";

const YES = 1;
const NO = 0;
const SOLVED = 2;

const MOVE = 3;

const CURSOR_WIDTH = 12;

const START_X = 147;
const START_Y = 2;

const END_X = 169;
const END_Y = 321;

var x = 147;
var y = 2;

const mazeWidth = 556;
const mazeHeight = 556;

var intervalVar;

function clearRectangle(px, py, w, h) {
    CONTEXT.beginPath();
    CONTEXT.rect(px, py, w, h);
    CONTEXT.closePath();
    CONTEXT.fillStyle = WHITE;
    CONTEXT.fill();
}

function drawRectangle(px, py, fillStyle) {
    CONTEXT.beginPath();
    CONTEXT.rect(px, py, CURSOR_WIDTH, CURSOR_WIDTH);
    CONTEXT.closePath();
    CONTEXT.fillStyle = fillStyle;
    CONTEXT.fill();
}

function drawCursor(px, py, fillStyle) {
    clearRectangle(x, y, CURSOR_WIDTH, CURSOR_WIDTH);
    x = px;
    y = py;
    drawRectangle(px, py, fillStyle)
}

function drawEndPoint(px, py, fillStyle) {
    const radius = 6;
    const startAngle = 0;
    const endAngle = 2 * Math.PI;
    const counterClockwise = false;

    CONTEXT.beginPath();
    CONTEXT.arc(px, py, radius, startAngle, endAngle, counterClockwise);
    CONTEXT.closePath();
    CONTEXT.fillStyle = fillStyle;
    CONTEXT.fill();
}


function drawMazeAndRectangle() {
    clearRectangle(0, 0, CANVAS.width, CANVAS.height);

    let mazeImg = new Image();
    mazeImg.onload = function () {
        CONTEXT.drawImage(mazeImg, 0, 0);
        drawCursor(START_X, START_Y, BLUE);
        drawEndPoint(END_X, END_Y, GREEN);
    };
    mazeImg.src = MAZE_IMG_PATH;
}

function moveRect(e) {
    const UP = 38;
    const LEFT = 37;
    const DOWN = 40;
    const RIGHT = 39;

    let point;
    e = e || window.event;
    switch (e.keyCode) {
        case UP:
            point = {px: x, py: y - MOVE};
            break;
        case LEFT:
            point = {px: x - MOVE, py: y};
            break;
        case DOWN:
            point = {px: x, py: y + MOVE};
            break;
        case RIGHT:
            point = {px: x + MOVE, py: y};
            break;
        default:
            return;
    }

    let movingAllowed = canMoveTo(point.px, point.py);
    if (movingAllowed === YES) {      // 1 means 'the rectangle can move'
        drawCursor(point.px, point.py, BLUE);
        x = point.px;
        y = point.py;
    }
    else if (movingAllowed === SOLVED) { // 2 means 'the rectangle reached the end point'
        clearInterval(intervalVar);
        clearRectangle(0, 0, CANVAS.width, CANVAS.height);
        CONTEXT.font = "40px Arial";
        CONTEXT.fillStyle = "blue";
        CONTEXT.textAlign = "center";
        CONTEXT.textBaseline = "middle";
        CONTEXT.fillText("Congratulations!", CANVAS.width / 2, CANVAS.height / 2);
        window.removeEventListener("keydown", moveRect, true);
    }
}

function isPixelBlack(imageData, pid) {
    return imageData[pid + RED_ID] === 0 && imageData[pid + GREEN_ID] === 0 && imageData[pid + BLUE_ID] === 0;
}

function isPixelGreen(imageData, pid) {
    return imageData[pid + RED_ID] === 0 && imageData[pid + GREEN_ID] === 255 && imageData[pid + BLUE_ID] === 0;
}

function canMoveTo(px, py) {
    const imgData = CONTEXT.getImageData(px, py, CURSOR_WIDTH, CURSOR_WIDTH);
    let canMove = YES;
    if (px >= 0 && px <= mazeWidth - CURSOR_WIDTH && py >= 0 && py <= mazeHeight - CURSOR_WIDTH) {
        for (let pix = 0; pix < 4 * 15 * 15; pix += 4) {
            if (isPixelBlack(imgData.data, pix)) {
                canMove = NO;
                break;
            }
            else if (isPixelGreen(imgData.data, pix)) {
                canMove = SOLVED;
                break;
            }
        }
    }
    else {
        canMove = NO;
    }
    return canMove;
}

function createTimer(seconds) {
    intervalVar = setInterval(function () {
        clearRectangle(mazeWidth, 0, CANVAS.width - mazeWidth, CANVAS.height);
        if (seconds === 0) {
            clearInterval(intervalVar);
            window.removeEventListener("keydown", moveRect, true);
            clearRectangle(0, 0, CANVAS.width, CANVAS.height);
            CONTEXT.font = "40px Arial";
            CONTEXT.fillStyle = "red";
            CONTEXT.textAlign = "center";
            CONTEXT.textBaseline = "middle";
            CONTEXT.fillText("Time's up!", CANVAS.width / 2, CANVAS.height / 2);
            return;
        }
        CONTEXT.font = "20px Arial";
        if (seconds <= 10 && seconds > 5) {
            CONTEXT.fillStyle = "orangered";
        }
        else if (seconds <= 5) {
            CONTEXT.fillStyle = "red";
        }
        else {
            CONTEXT.fillStyle = "green";
        }
        CONTEXT.textAlign = "center";
        CONTEXT.textBaseline = "middle";
        var minutes = Math.floor(seconds / 60);
        var secondsToShow = (seconds - minutes * 60).toString();
        if (secondsToShow.length === 1) {
            secondsToShow = "0" + secondsToShow; // if the number of seconds is '5' for example, make sure that it is shown as '05'
        }
        CONTEXT.fillText(minutes.toString() + ":" + secondsToShow, mazeWidth + 30, CANVAS.height / 2);
        seconds--;
    }, 1000);
}

drawMazeAndRectangle();
window.addEventListener("keydown", moveRect, true);
createTimer(120); // 2 minutes
