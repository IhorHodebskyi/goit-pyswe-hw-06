SELECT g.name AS group_name, AVG(gr.grade) AS average_grade
FROM groups g
JOIN students st ON g.id = st.group_id
JOIN grades gr ON st.id = gr.student_id
JOIN subjects sub ON gr.subject_id = sub.id
WHERE sub.name = 'Math'
GROUP BY g.name;