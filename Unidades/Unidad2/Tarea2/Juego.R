# SIMULACION: JUEGO DE INTERCAMBIO DE DULCES
juego_dulces <- function(jugadores = 4, max_iter = 100000) {

  dulce_random <- function() sample(c("A","B","C"),1)

  quitar_combo <- function(pool) {
    for (tipo in c("A","B","C")) {
      pos <- match(tipo , pool)
      if (!is.na(pos)) pool <- pool[-pos]
    }
    return(pool)
  }

  quitar_n <- function(pool , tipo , n) {
    pos <- which(pool == tipo)
    if (length(pos) >= n) pool <- pool[-pos[1:n]]
    return(pool)
  }

  set.seed(as.integer(Sys.time()))
  pool <- replicate(jugadores * 2, dulce_random ())
  D <- 0

  iter <- 0
  while (iter < max_iter && D < jugadores) {
    iter <- iter + 1
    cambio <- FALSE

    a <- sum(pool == "A")
    b <- sum(pool == "B")
    c <- sum(pool == "C")

    combos_dobles <- min(floor(a/2), floor(b/2), floor(c/2))
    while (combos_dobles > 0) {
      pool <- quitar_n(pool , "A", 2)
      pool <- quitar_n(pool , "B", 2)
      pool <- quitar_n(pool , "C", 2)
      D <- D + 2
      pool <- c(pool , dulce_random())
      cambio <- TRUE
      combos_dobles <- combos_dobles - 1
    }

    combos_simples <- min(a, b, c)
    while (combos_simples > 0) {
      pool <- quitar_combo(pool)
      D <- D + 1
      cambio <- TRUE
      combos_simples <- combos_simples - 1
    }

    if (!cambio && D > 0) {
      D <- D - 1
      pool <- c(pool , replicate (3, dulce_random()))
      cambio <- TRUE
    }

    if (!cambio && D == 0 && !all(c("A","B","C") %in% pool)) break
  }

  return(list(D = D, iter = iter, exito = (D >= jugadores)))
}

juego_dulces(4)