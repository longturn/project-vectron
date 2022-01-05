add_side <- function(type = c('plains', 'grassland', 'forest', 'desert', 'tundra', 'ice'),
					  side = c('left','down','right'), col, row) {

	type <-match.arg(type)
	side <- match.arg(side)

	row_skip <- -24.261992 - -51.392991
	col_skip <- 369.92537 - 274.1462

	if (type == 'plains') {
		if (side == 'left')
			parent <- '#g6911'
		if (side == 'down')
			parent <- '#g6921'
		if (side == 'right')
			parent <- '#g6916'

		id <- 'use16764-111'
		col_0 <- 274.1462
		row_0 <- -51.392991
	}

	if (type == 'grassland') {
		if (side == 'left')
			parent <- '#g7258'
		if (side == 'down')
			parent <- '#g7358'
		if (side == 'right')
			parent <- '#g7440'

		col_0 <- 274.14562
		row_0 <- -77.851262
	}

	if (type == 'forest') {
		if (side == 'left')
			parent <- '#g7625'
		if (side == 'down')
			parent <- '#g7991'
		if (side == 'right')
			parent <- '#g7828'

		col_0 <- 274.14678
		row_0 <- -104.3097
	}

	if (type == 'desert') {
		if (side == 'left')
			parent <- '#g4463'
		if (side == 'down')
			parent <- '#g4466'
		if (side == 'right')
			parent <- '#g4469'

		col_0 <- 274.14678
		row_0 <- -130.76786
	}

	if (type == 'tundra') {
		if (side == 'left')
			parent <- '#g7995'
		if (side == 'down')
			parent <- '#g8000'
		if (side == 'right')
			parent <- '#g4525'

		col_0 <- 274.14504
		row_0 <- -157.22616
	}

	if (type == 'ice') {
		if (side == 'left')
			parent <- '#g8046'
		if (side == 'down')
			parent <- '#g8043'
		if (side == 'right')
			parent <- '#g8049'

		col_0 <- 274.14562
		row_0 <- -183.6846
	}

	return(paste0('    <use
       x="0"
       y="0"
       xlink:href="', parent, '"
       id=""
       transform="translate(', col_0 + col_skip * col,',', row_0 + row_skip * row, ')"
       width="100%"
       height="100%" />\n'))
}



sprites <- c('plains', 'grassland', 'forest', 'desert', 'tundra', 'ice')

combinations <- expand.grid(sprites,sprites,sprites)
combinations$row <- rep(0:35, 6)
combinations$col <- rep(0:5, each = nrow(combinations)/6)

sink("test_file.txt")
for(y in 1:nrow(combinations)) {
	for (x in 1:3) {
		cat(add_side(type = as.character(combinations[y,x]), 
					 side = c('left','down','right')[x], 
					 col = combinations$col[y], row = combinations$row[y]))
	}
}
sink()