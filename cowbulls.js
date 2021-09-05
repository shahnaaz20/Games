function main() {
    var len = 4;
    playBullsAndCows(len);
}
 
function playBullsAndCows(len) {
    var num = pickNum(len);
    //console.log('The secret number is:\n  ' + num.join('\n  '));
    showInstructions(len);
    var nGuesses = 0;
    while (true) {
        nGuesses++;
        var guess = getGuess(nGuesses, len);
        var census = countBovine(num, guess);
        showScore(census.bulls, census.cows);
        if (census.bulls == len) {
            showFinalResult(nGuesses);
            return;
        }
    }
}
 
function showScore(nBulls, nCows) {
    console.log('    Bulls: ' + nBulls + ', cows: ' + nCows);
}
 
function showFinalResult(guesses) {
    console.log('You win!!! Guesses needed: ' + guesses);
}
 
function countBovine(num, guess) {
    var count = {bulls:0, cows:0};
    var g = guess.join('');
    for (var i = 0; i < num.length; i++) {
        var digPresent = g.search(num[i]) != -1;
        if (num[i] == guess[i]) count.bulls++;
        else if (digPresent) count.cows++;
    }
    return count;
}
 
function getGuess(nGuesses, len) {
    while (true) {
        console.log('Your guess #' + nGuesses + ': ');
        var guess = readline();
        guess = String(parseInt(guess)).split('');
        if (guess.length != len) {
            console.log('  You must enter a ' + len + ' digit number.');
            continue;
        }
        if (hasDups(guess)) {
            console.log('  No digits can be duplicated.');
            continue;
        }    
        return guess;
    }
}
 
function hasDups(ary) {
    var t = ary.concat().sort();
    for (var i = 1; i < t.length; i++) {
        if (t[i] == t[i-1]) return true;
    }
    return false;
}
 
function showInstructions(len) {
    console.log();
    console.log('Bulls and Cows Game');
    console.log('-------------------');
    console.log('  You must guess the ' + len + ' digit number I am thinking of.');
    console.log('  The number is composed of the digits 1-9.');
    console.log('  No digit appears more than once.');
    console.log('  After each of your guesses, I will tell you:');
    console.log('    The number of bulls (digits in right place)');
    console.log('    The number of cows (correct digits, but in the wrong place)');
    console.log();
}
 
function pickNum(len) {
    var nums = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    nums.sort(function(){return Math.random() - 0.5});
    return nums.slice(0, len);
}
main();