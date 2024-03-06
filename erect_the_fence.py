# Using Distance Formula
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # Function to determine if three points are in clockwise order
        def clockwise(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            
            # Calculate the cross product
            return ((y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2))
        
        # Sort the input trees lexicographically
        trees.sort()
        
        # Initialize lists to store points forming upper and lower hulls
        upper = []
        lower = []
        
        # Iterate through each tree
        for t in trees:
            # Update the upper hull
            while len(upper) > 1 and clockwise(upper[-2], upper[-1], t) > 0:
                upper.pop()
            # Update the lower hull
            while len(lower) > 1 and clockwise(lower[-2], lower[-1], t) < 0:
                lower.pop()
            # Add the current tree to both upper and lower hulls
            upper.append(tuple(t))
            lower.append(tuple(t))
            
        # Combine the upper and lower hulls and convert to a set to remove duplicates
        return list(set(upper + lower))

# Graham Scan Algorithm
class Solution:
  def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
    # The orientation function determines the relative orientation of the triplet (p, q, r).
    # If the result is 0, they're collinear.
    # If the result is positive, the triplet is in counterclockwise order.
    # If the result is negative, the triplet is in clockwise order.
    def orientation(p, q, r):
      return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])
    
    # Sort the points based on their x-coordinate, and if they have the same x-coordinate,
    # sort based on their y-coordinate.
    points.sort(key=lambda p: (p[0], p[1]))
    
    # Initialize an empty list to store the points of the convex hull.
    hull = []
    
    # The first loop constructs the lower part of the convex hull.
    for point in points:
      # If the current point doesn't make a counterclockwise turn from the last two points in the hull,
      # remove the last point from the hull.
      while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) < 0:
        hull.pop()
      # Append the current point to the hull.
      # Have to cast to tuple becauses lists are not hashable since they are mutable unlike immutable tuples
      hull.append(tuple(point))
    
    # The second loop constructs the upper part of the convex hull.
    # We skip the last point in the sorted list as it's already included.
    for point in reversed(points[:-1]):
      # Similar to the first loop, if the current point doesn't make a counterclockwise turn from the last two points in the hull,
      # points in the hull, remove the last point from the hull.
      while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) < 0:
        hull.pop()
      # Append the current point to the hull.
      # Have to cast to tuple becauses lists are not hashable since they are mutable unlike immutable tuples
      hull.append(tuple(point))
    
    # Some points might be included in the hull twice (once from the lower part and once from the upper part).
    # Convert the hull to a set and then back to a list to remove any redundant points.
    return list(set(hull))
