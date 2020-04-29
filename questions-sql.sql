DROP TABLE IF EXISTS public.questions;
CREATE TABLE public.questions (id INTEGER PRIMARY KEY , submission_time timestamp, view_number INTEGER, vote_number INTEGER, title TEXT, message TEXT, image TEXT);
INSERT INTO public.questions (id, submission_time, view_number, vote_number, title, message, image) VALUES (1,'2020-04-29 12:02:33', 29 , 7 ,'How to make lists in Python?','I am totally new to this, any hints?', null);
INSERT INTO public.questions (id, submission_time, view_number, vote_number, title, message, image) VALUES (2, '2020-04-29 12:02:51', 15, 9, 'Wordpress loading multiple jQuery Versions', 'I developed a plugin that uses the jquery booklet plugin (http://builtbywill.com/booklet/#/) this plugin binds a function to $ so I cann call $(''.myBook'').booklet();

I could easy managing the loading order with wp_enqueue_script so first I load jquery then I load booklet so everything is fine.

BUT in my theme i also using jquery via webpack so the loading order is now following:

jquery
booklet
app.js (bundled file with webpack, including jquery)', 'images/image1.png');
INSERT INTO public.questions (id, submission_time, view_number, vote_number, title, message, image) VALUES (3, '2020-04-29 12:03:13', 1364, 57, 'Drawing canvas with an image picked with Cordova Camera Plugin', 'I''m getting an image from device and drawing a canvas with filters using Pixi JS. It works all well using computer to get an image. But when I''m on IOS, it throws errors such as cross origin issue, or that I''m trying to use an unknown format.

This is the code I''m using to draw the image (that works on web/desktop but not cordova built ios app)', null);