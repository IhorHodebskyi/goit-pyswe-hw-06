SELECT s.name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.name
ORDER BY average_grade DESC
LIMIT 5;