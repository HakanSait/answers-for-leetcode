function halvesAreAlike(s: string): boolean {
    const vowels: Set<string> = new Set<string>(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);

    let vowelsInPartOne: number = 0;
    let vowelsInPartTwo: number = 0;

    for (let i: number = 0; i < s.length / 2; i++) {
        if (vowels.has(s[i])) {
            vowelsInPartOne++;
        }

        if (vowels.has(s[i + s.length / 2])) {
            vowelsInPartTwo++;
        }
    }


    return vowelsInPartOne === vowelsInPartTwo;
}
