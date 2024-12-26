// let particles = document.getElementsByClassName("particle");

// //  for (i of particles) {
// //     i.style.top = (Math.random()*90)+10;
// //     i.style.left = (Math.random()*90)+10;
// //     class goal {
// //         x = Math.random()*200+300;
// //         y = Math.random()*200+300;
// //     }
// //     g = new goal();
// //     setInterval(() => {
// //         x = Number(i.style.left.replace('px', ''));
// //         y = Number(i.style.top.replace('px', ''));
// //         console.log(g.x, g.y, x, y);
// //         if(y < g.y && x < g.x) {
// //             var ratio = g.y/g.x;
// //             i.style.top += (ratio+"px");
// //             i.style.left = ((x + 1)+"px");
// //             console.log(g.x+", "+g.y);
// //         }
// //         else {console.log("Goal reached")}
// //     }, 50);
// //  }

// function setX(i, x) {
//     i.style.left = x+'px';
// }

// function setY(i, y) {
//     i.style.top = y+'px';
// }

// function getX(i) {
//     return Number(i.style.left.replace('px', ''));
// }

// function getY(i) {
//     return Number(i.style.top.replace('px', ''));
// }

// var goalDiv = document.getElementsByClassName("goal")[0];

// for (i of particles) {
//     setX(i, Math.round(Math.random()*90)+10);
//     setY(i, Math.round(Math.random()*90)+10);

//     class Goal {
//         constructor() {
//             this.x = Math.round(Math.random()*200+300);
//             this.y = Math.round(Math.random()*200+300);
//         }

//         newGoal() {
//             this.x = Math.round(Math.random()*200+300);
//             this.y = Math.round(Math.random()*200+300);
//         }
//     }

//     goal = new Goal();

//     setX(goalDiv, goal.x);
//     setY(goalDiv, goal.y);

//     xSlope = Math.abs(goal.x-getX(i))/100;
//     ySlope = Math.abs(goal.y-getY(i))/100;


//     window.setInterval(function() {
//         console.log(getX(i), getY(i), goal.x, goal.y)
//     if (getX(i) < goal.x) {
//         setX(i, (getX(i)+(xSlope)));
//     } else if (getX(i) > goal.x) {
//         setX(i, (getX(i)-(xSlope)));
//     }

//     if (getY(i) < goal.y) {
//         setY(i, (getY(i)+(ySlope)));
//     } else if (getY(i) > goal.y) {
//         setY(i, (getY(i)-(ySlope)));
//     }

//     if (getY(i) == goal.y && getX(i) == goal.x) {
//         goal.newGoal();

//         setX(goalDiv, goal.x);
//         setY(goalDiv, goal.y);
//     }

//     }, 100);

// }

