vector<int> gradingStudents(vector<int> grades) {
    int p;
    for(int i=0;i<grades.size();i++)
    {    
        if(grades[i]>=38)
        {
            p=grades[i]%5;
            if(p>=3)
            {
                grades[i]=grades[i]+5-p;
            }
        }
    }
return grades;
}
