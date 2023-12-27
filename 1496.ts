function isPathCrossing(path: string): boolean {
    let x: number = 0;
    let y: number = 0;

    for (let i: number = 0; i < path.length; i++) {
        switch (path[i]) { 
            case 'N':
                y++;
                break;

            case 'S':
                y--;
                break;

            case 'E':
                x++;
                break;

            case 'W':
                x--;
                break;

            default:
                return false;
        }

        if (
            x == 0 &&
            y == 0
        ) {
            return true;
        }
    }

    return false;
}
