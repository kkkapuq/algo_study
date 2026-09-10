select b.user_id, b.nickname, sum(a.price) as total_sales
  from used_goods_board a, used_goods_user b
 where a.writer_id = b.user_id
   and a.status = 'DONE'
 group by b.user_id, b.nickname
 having total_sales >= 700000
 order by total_sales