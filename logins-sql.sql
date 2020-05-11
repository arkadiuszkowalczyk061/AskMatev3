DROP TABLE IF EXISTS public.user_login;
CREATE TABLE public.user_login (id INTEGER PRIMARY KEY, login varchar(16) UNIQUE not null);
INSERT INTO public.user_login (id, login) VALUES (1, 'hajto');
