DROP TABLE IF EXISTS public.answers;
CREATE TABLE public.answers (id INTEGER PRIMARY KEY, submission_time INTEGER, vote_number INTEGER, question_id INTEGER, message TEXT);
INSERT INTO public.answers (id, submission_time, vote_number, question_id, message) VALUES (2, 1493088154, 35, 1, 'Look it up in the Python docs');