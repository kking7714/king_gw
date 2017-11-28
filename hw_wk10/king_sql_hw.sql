
use sakila;
-- 1a. Display the first and last names of all actors from the table actor
select first_name, last_name from actor;

-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
select concat(first_name, ' ' , last_name) as Actor_Name from actor;

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?`
select actor_id, first_name, last_name from actor where first_name like 'JOE';

-- 2b. Find all actors whose last name contain the letters GEN:
select actor_id, first_name, last_name from actor where last_name like '%GEN%';

-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
select actor_id, first_name, last_name from actor where last_name like '%LI%' order by last_name, first_name;

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
select country_id, country from country where country in ('Afghanistan','Bangladesh','China');

-- 3a. Add a middle_name column to the table actor. Position it between first_name and last_name. Hint: you will need to specify the data type.
alter table actor add middle_name varchar(50);

-- 3b. You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.
alter table actor alter column middle_name blob;

-- 3c. Now delete the middle_name column.
alter table actor drop column middle_name;

-- 4a. List the last names of actors, as well as how many actors have that last name.
select distinct last_name, count(last_name) as Last_Name_Count from actor group by last_name;

-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
select distinct last_name, count(last_name) as Last_Name_Count from actor group by last_name having count(*) >=2;

-- 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
select * from actor where last_name like 'WILLIAMS';
update actor set first_name='HARPO' where actor_id=172;

-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query,
--  if the first name of the actor is currently HARPO, change it to GROUCHO. Otherwise, change the first name to MUCHO GROUCHO, as that is exactly 
--  what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER! 
--  (Hint: update the record using a unique identifier.)
update actor set first_name='GROUCHO' where first_name='HARPO';

-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
select * from information_schema.columns where table_name='address';

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
select staff.first_name, staff.last_name, address.address
from staff 
join address on staff.address_id = address.address_id;

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
select s.first_name, s.last_name, s.staff_id, sum(p.amount )as totalamount
from staff s
join payment p on p.staff_id = s.staff_id
group by s.staff_id;

-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
select f.film_id, f.title, count(a.actor_id) as ActorCount
from film f
join film_actor a on f.film_id = a.film_id
group by f.film_id;

-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
select * from film where title like 'Hunchback Impossible';
select count(film_id) as InventoryCount from inventory where film_id = 439;

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
select c.first_name, c.last_name, c.customer_id, sum(p.amount )as 'Total Amount Paid'
from customer c
join payment p on p.customer_id = c.customer_id
group by c.customer_id
order by c.last_name, c.first_name;

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended 
-- consequence, films starting with the letters K and Q have also soared in popularity. Use subqueries to display t
-- he titles of movies starting with the letters K and Q whose language is English.
select * from film where language_id like "1" and title like "Q%" or title like "K%";

-- 7b. Use subqueries to display all actors who appear in the film Alone Trip
select a.first_name, a.last_name, f.title
from film_actor fa
join actor a on a.actor_id = fa.actor_id
join film f on f.film_id = fa.film_id
where f.title = 'Alone Trip';

-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and 
-- email addresses of all Canadian customers. Use joins to retrieve this information.
select cu.first_name, cu.last_name, cu.email, ci.country_id
from customer cu
join address a on a.address_id = cu.address_id
join city ci on ci.city_id = a.city_id
where ci.country_id = "20";

-- 7d. Sales have been lagging among young families, and you wish to target all family movies 
-- for a promotion. Identify all movies categorized as famiy films.
select * from film
where rating like 'G' or rating like 'PG';

-- 7e. Display the most frequently rented movies in descending order.
select * from film 
order by rental_rate desc;

-- 7f. Write a query to display how much business, in dollars, each store brought in.
select sum(p.amount) as 'Total Sales', s.store_id
from payment p
join staff st on st.staff_id = p.staff_id
join store s on s.store_id = st.staff_id
group by s.store_id;

-- 7g. Write a query to display for each store its store ID, city, and country.
select s.store_id, c.city, co.country
from store s
join address a on a.address_id = s.address_id
join city c on c.city_id = a.city_id
join country co on co.country_id = c.country_id;

-- 7h. List the top five genres in gross revenue in descending order. 
-- (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
select ca.name as 'Gengre', sum(p.amount) as 'Total'
from category ca
join film_category fc on fc.category_id = ca.category_id
join inventory i on i.film_id = fc.film_id
join rental r on r.inventory_id = i.inventory_id
join payment p on p.rental_id = r.rental_id
group by ca.name;

-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres 
-- by gross revenue. Use the solution from the problem above to create a view. 
-- If you haven't solved 7h, you can substitute another query to create a view.
create view top_five_genre as
select ca.name as 'Gengre', sum(p.amount) as 'Total'
from category ca
join film_category fc on fc.category_id = ca.category_id
join inventory i on i.film_id = fc.film_id
join rental r on r.inventory_id = i.inventory_id
join payment p on p.rental_id = r.rental_id
group by ca.name
order by 'Total' desc limit 5;

-- 8b. How would you display the view that you created in 8a?
select * from top_five_genre;

-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
drop view top_five_genre;