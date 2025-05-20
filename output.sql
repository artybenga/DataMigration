select
	r.matter_id
	,c.id as client_id
	,case m."Opened"
		when 'true' then 'Open'
		when 'false' then 'Closed'
	end as Status
	,m."Description"
	,to_char(to_date(m."Open Date", 'YYYY-MM-DD'), 'MM/DD/YYYY') as OpenDate
	,case
		when c."Name" like '% %' then SPLIT_PART(c."Name", ' ', 1)
		when c."Name" like '%_' then ''
		else ''
	end as first_name
	,SPLIT_PART(c."Name", ' ', 2) AS last_name
	,SPLIT_PART(c."Name", '_', 2) AS company
	-- ,m.*
	-- ,c.*
from contacts c
left join related r on r.contact_id = c.id
left join matters m on m.matter_id = r.matter_id