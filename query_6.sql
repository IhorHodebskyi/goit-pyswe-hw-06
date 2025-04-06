SELECT s.name
FROM students s
JOIN groups g ON s.group_id = g.id
WHERE g.name = 'Group A';
