# Asked in Goldman Sachs Strats Interview 
def whoIsElected(n, k):
        """ 
        A group of students are sitting in a circle. The teacher is electing a new class president. 
        The teacher does this by singing a song while walking around the circle. After the song is 
        finished the student at which the teacher stopped is removed from the circle. 

        Starting at the student next to the one that was just removed, the teacher resumes singing and walking around the circle.
        After the teacher is done singing, the next student is removed. The teacher repeats this until only one student is left. 

        A song of length k will result in the teacher walking past k students on each round. The students are numbered 1 to n. 
        The teacher begins at the first student. 

        For example, suppose the song length is two (k=2). And there are four students to start with (1,2,3,4). The first 
        student to go would be `2`, after that `4`, and after that `3`. Student `1` would be the next president in this example.
     
        @param n:   the number of students sitting in a circle.
        @param k:   the length (in students) of each song.
        @return:    the number of the student that is elected.
        """
        
        students = []
        
        for i in range(1, n + 1):
            students.append(i)
        
        for j in range(n - 1): # O(n * k) 
            for i in range(1, k):
                x = students.pop(0)
                students.append(x)
            students.pop(0)
                
        return students[0]  
