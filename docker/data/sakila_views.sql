CREATE VIEW query4a AS
  SELECT last_name, COUNT(*) AS "Last Name Count"
  FROM actor
  GROUP BY last_name
  ORDER BY last_name;

CREATE VIEW query4b AS
  SELECT last_name, COUNT(*) AS "Last Name Count"
  FROM actor
  GROUP BY last_name
  HAVING COUNT(*) >=2;


CREATE VIEW query6b AS
  SELECT first_name, last_name, SUM(amount) as "Total Amount"
  FROM staff
  INNER JOIN payment ON staff.staff_id = payment.staff_id
  AND payment.payment_date >= '2005-08-01'::date
  GROUP BY first_name, last_name;


CREATE VIEW query6c AS
  SELECT title, COUNT(actor_id) as "Actor Count"
  FROM film_actor INNER JOIN film
  ON film_actor.film_id = film.film_id
  GROUP BY title
  ORDER BY title;


CREATE VIEW query6e AS
  SELECT first_name, last_name, SUM(amount) as "Total Paid by Each Customer"
  FROM payment
  INNER JOIN customer ON payment.customer_id = customer.customer_id
  GROUP BY first_name, last_name
  ORDER BY last_name;


CREATE VIEW query7a AS
  SELECT title
  FROM film
  WHERE title LIKE 'K%'
  OR title LIKE 'Q%'
  AND title IN (
    SELECT title
    FROM film
    WHERE language_id IN (
      SELECT language_id
      FROM "language"
      WHERE name ='English'
    )
  );


CREATE VIEW query7b AS
  SELECT first_name, last_name
  FROM actor
  WHERE actor_id IN (
    SELECT actor_id
    FROM film_actor
    WHERE film_id IN (
       SELECT film_id
       FROM film
       WHERE title = 'Alone Trip'
    )
  );


CREATE VIEW query7c AS
  SELECT first_name, last_name, email
  FROM customer
  JOIN address ON (customer.address_id = address.address_id)
  JOIN city ON (city.city_id = address.city_id)
  JOIN country ON (country.country_id = city.country_id)
  WHERE country.country= 'Canada';


CREATE VIEW query7e AS
  SELECT title, COUNT(rental_id) as "Rental Count"
  FROM rental
  JOIN inventory ON (rental.inventory_id = inventory.inventory_id)
  JOIN film ON (inventory.film_id = film.film_id)
  GROUP BY film.title
  ORDER BY COUNT(rental_id) DESC;


CREATE VIEW query7f AS
  SELECT store.store_id, SUM(amount)
  FROM store
  INNER JOIN staff ON store.store_id = staff.store_id
  INNER JOIN payment ON payment.staff_id = staff.staff_id
  GROUP BY store.store_id;


CREATE VIEW query7h AS
  SELECT name, SUM(amount)
  FROM category
  INNER JOIN film_category ON category.category_id = film_category.category_id
  INNER JOIN inventory ON film_category.film_id = inventory.film_id
  INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
  INNER JOIN payment ON rental.rental_id = payment.rental_id
  GROUP BY name
  ORDER BY SUM(amount) DESC LIMIT 5;