-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 28-09-2022 a las 21:08:43
-- Versión del servidor: 5.7.33
-- Versión de PHP: 8.1.8

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `python_fonasa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comunas`
--

CREATE TABLE `comunas` (
  `id` int(11) NOT NULL,
  `region_id` int(11) NOT NULL DEFAULT '0',
  `comuna` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Comunas de la region metropolitana';

--
-- Volcado de datos para la tabla `comunas`
--

INSERT INTO `comunas` (`id`, `region_id`, `comuna`, `created_at`) VALUES
(1, 0, 'Cerrillos', '2022-09-28 15:20:37'),
(2, 0, 'Cerro Navia', '2022-09-28 15:20:59'),
(3, 0, 'Conchalí', '2022-09-28 15:20:59'),
(4, 0, 'El Bosque', '2022-09-28 15:22:09'),
(5, 0, 'Estación Central', '2022-09-28 15:22:09'),
(6, 0, 'Huechuraba', '2022-09-28 15:22:09'),
(7, 0, 'Independencia', '2022-09-28 15:22:09'),
(8, 0, 'La Cisterna', '2022-09-28 15:22:09'),
(9, 0, 'La Florida', '2022-09-28 15:23:43'),
(10, 0, 'La Granja', '2022-09-28 15:23:43'),
(11, 0, 'La Pintana', '2022-09-28 15:23:43'),
(12, 0, 'La Reina', '2022-09-28 15:23:43'),
(13, 0, 'Las Condes', '2022-09-28 15:23:43'),
(14, 0, 'Lo Barnechea', '2022-09-28 15:23:43'),
(15, 0, 'Lo Espejo', '2022-09-28 15:23:43'),
(16, 0, 'Lo Prado', '2022-09-28 15:23:43'),
(17, 0, 'Macul', '2022-09-28 15:23:43'),
(18, 0, 'Maipú', '2022-09-28 15:23:43'),
(19, 0, 'Ñuñoa', '2022-09-28 15:25:04'),
(20, 0, 'Padre Hurtado', '2022-09-28 15:25:04'),
(21, 0, 'Pedro Aguirre Cerda', '2022-09-28 15:25:04'),
(22, 0, 'Peñalolén', '2022-09-28 15:25:04'),
(23, 0, 'Pirque', '2022-09-28 15:25:04'),
(24, 0, 'Providencia', '2022-09-28 15:25:04'),
(25, 0, 'Pudahuel', '2022-09-28 15:25:04'),
(26, 0, 'Puente Alto', '2022-09-28 15:25:04'),
(27, 0, 'Quilicura', '2022-09-28 15:25:04'),
(28, 0, 'Quinta Normal', '2022-09-28 15:25:04'),
(29, 0, 'Recoleta', '2022-09-28 15:26:27'),
(30, 0, 'Renca', '2022-09-28 15:26:27'),
(31, 0, 'San Bernardo', '2022-09-28 15:26:27'),
(32, 0, 'San Joaquín', '2022-09-28 15:26:27'),
(33, 0, 'San José de Maipo', '2022-09-28 15:26:27'),
(34, 0, 'San Miguel', '2022-09-28 15:26:27'),
(35, 0, 'San Ramón', '2022-09-28 15:26:27'),
(36, 0, 'Santiago', '2022-09-28 15:26:27');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `institution`
--

CREATE TABLE `institution` (
  `id` int(11) NOT NULL,
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `direction` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `comuna_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Tabla Establecimiento Medico';

--
-- Volcado de datos para la tabla `institution`
--

INSERT INTO `institution` (`id`, `name`, `direction`, `comuna_id`, `created_at`) VALUES
(2, 'Centro 101', 'Santiago centro', 13, '2022-09-28 15:32:07'),
(3, 'My centro', 'Av. La Paz 477', 29, '2022-09-28 15:50:02'),
(4, 'El Centro medico', 'Avenida Independencia 1133', 7, '2022-09-28 15:54:28');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `patients`
--

CREATE TABLE `patients` (
  `id` int(11) NOT NULL,
  `rut` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `fullname` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `age` int(11) NOT NULL,
  `weight` float NOT NULL,
  `height` int(11) NOT NULL,
  `smoker` varchar(2) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'NO',
  `smoker_time` int(2) NOT NULL DEFAULT '0',
  `diet` varchar(2) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'NO',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Tabla paciente';

--
-- Volcado de datos para la tabla `patients`
--

INSERT INTO `patients` (`id`, `rut`, `fullname`, `age`, `weight`, `height`, `smoker`, `smoker_time`, `diet`, `created_at`) VALUES
(1, '26974050-7', 'Haleym Hidalgo Moyeones', 42, 128.5, 182, 'SI', 5, 'NO', '2022-09-28 18:58:49'),
(3, '26937727-5', 'Natali Torres', 39, 62, 159, 'NO', 0, 'SI', '2022-09-28 20:47:32');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `specialist`
--

CREATE TABLE `specialist` (
  `id` int(11) NOT NULL,
  `fullname` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `specialty_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Tabla Especilasta';

--
-- Volcado de datos para la tabla `specialist`
--

INSERT INTO `specialist` (`id`, `fullname`, `specialty_id`, `created_at`) VALUES
(1, 'hah', 2, '2022-09-27 21:45:21'),
(2, 'mamam', 1, '2022-09-27 21:52:59'),
(4, 'dfdbcvb', 1, '2022-09-27 21:53:13');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `specialty`
--

CREATE TABLE `specialty` (
  `id` int(11) NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Tabla Especialidades';

--
-- Volcado de datos para la tabla `specialty`
--

INSERT INTO `specialty` (`id`, `name`, `created_at`) VALUES
(1, 'Pediatría', '2022-09-27 17:54:29'),
(2, 'Oftalmología', '2022-09-27 17:54:29'),
(5, 'mi especialidad', '2022-09-27 18:56:29');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `comunas`
--
ALTER TABLE `comunas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `institution`
--
ALTER TABLE `institution`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rut` (`rut`);

--
-- Indices de la tabla `specialist`
--
ALTER TABLE `specialist`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `specialty`
--
ALTER TABLE `specialty`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `comunas`
--
ALTER TABLE `comunas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT de la tabla `institution`
--
ALTER TABLE `institution`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `patients`
--
ALTER TABLE `patients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `specialist`
--
ALTER TABLE `specialist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `specialty`
--
ALTER TABLE `specialty`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
SET FOREIGN_KEY_CHECKS=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
