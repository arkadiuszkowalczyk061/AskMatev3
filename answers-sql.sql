DROP TABLE IF EXISTS public.answers;
CREATE TABLE public.answers (id INTEGER PRIMARY KEY, submission_time TIMESTAMP, vote_number INTEGER, question_id INTEGER, message TEXT);
INSERT INTO public.answers (id, submission_time, vote_number, question_id, message) VALUES (1, '2020-04-29 12:01:06
', 4 ,1 , 'You need to use brackets: my_list = []'), (2, '2020-04-29 12:02:00', 35, 1, 'Look it up in the Python docs');
