SELECT sub.name
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
JOIN students s ON g.student_id = s.id
JOIN teachers t ON sub.teacher_id = t.id
WHERE s.name = 'Ihor' AND t.name = 'John Doe';
