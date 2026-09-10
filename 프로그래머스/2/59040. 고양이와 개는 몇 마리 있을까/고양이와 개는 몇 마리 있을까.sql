select animal_type, count(*)
  from animal_ins
 where animal_type = 'Dog'
    or animal_type = 'Cat'
 group by animal_type
 order by animal_type 