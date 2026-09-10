select c.author_id, c.author_name, a.category, sum(a.price * b.sales) as total_prices
  from book a, book_sales b, author c
 where a.book_id = b.book_id
   and a.author_id = c.author_id
   and b.sales_date >= to_date('20220101', 'yyyymmdd')
   and b.sales_date < to_date('20220201', 'yyyymmdd')
 group by c.author_id, c.author_name, a.category
 order by c.author_id, a.category desc
 