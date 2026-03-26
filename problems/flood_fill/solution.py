class Solution(object):
    def floodFill(self, image, sr, sc, color):
        if not image:
            return image
        original_color = image[sr][sc]
        if original_color == color:
            return image
        image[sr][sc] = color
        directions = [0,1], [0, -1], [1, 0], [-1, 0]
        for dr, dc in directions:
            new_sr, new_sc = sr + dr, sc + dc
            if 0 <= new_sr < len(image) and 0 <= new_sc < len(image[0]) and image[new_sr] [new_sc] == original_color:
                self.floodFill(image, new_sr, new_sc, color)
        return image