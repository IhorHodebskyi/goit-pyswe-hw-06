SELECT s.name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.name = 'Math' 
GROUP BY s.name
ORDER BY average_grade DESC
LIMIT 1;