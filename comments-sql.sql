DROP TABLE IF EXISTS public.comments;
CREATE TABLE public.comments (id BIGSERIAL PRIMARY KEY NOT NULL, message text not null, question_id INT not null , answer_id INT not null );
INSERT INTO public.comments (id, message, question_id, answer_id) VALUES (1, 'xDD', 1, 1);
