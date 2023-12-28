function isPalindrome(x: number): boolean {
    if (x < 0) {
        return false;
    }

    let xReversed: number = 0;

    let xOriginal: number = x;
    while (x != 0) {
        xReversed = (xReversed * 10) + (x % 10);
        x = Math.floor(x / 10);
    }

    return xReversed === xOriginal;
}
