from math import sqrt


class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        a2=self.a+self.b

        if a2>self.c or self.b+self.c>self.a or self.a+self.c>self.b:
            return True
        else:
            return False
        
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.

        Note: typies are 'Teng yonli', 'Teng tomonli', 'Turli tomonli'
        '''
        if self.a == self.b:
            return 'Teng yonli'
        if self.a==self.b==self.c:
            return 'Teng tomonli'
        if self.a!=self.b!=self.c:
            return 'Turli tomonli'
        
    def perimeter(self) -> float:
        '''
        This method finds the perimeter of the triangle.
        Args:
            No
        Returns:
            float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        
        a1= self.a+self.b+self.c
        return a1

    def area(self) -> float:
        '''
        This method finds the area of the triangle.
        Args:
            NO
        Returns:
            float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        p=(self.a+self.b+self.c)/2
        s=sqrt((p-self.a)*(p-self.b)*(p-self.c))
        return s
