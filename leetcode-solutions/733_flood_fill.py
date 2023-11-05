class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color: # whats trying to be flood filled is the target color already.
            return image # return because no changes would be made


        originalColor = image[sr][sc] # Keep track of what the color was originally
        image[sr][sc] = color # image at this point should be changed to the new color passed in.

        # Define the possible moves (up, down, left, right)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in moves: # check all around the pixel from argument (4 directions)
            nr, nc = sr + dr, sc + dc # new column, new row that we want to focus on. 
            if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == originalColor: # check nc/nr within img size; check nc/nr are the original col
                self.floodFill(image, nr, nc, color) # recursive call to then apply to this verified pixel

        return image