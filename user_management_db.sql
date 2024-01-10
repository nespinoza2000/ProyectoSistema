-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-01-2024 a las 00:14:15
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `user_management_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `camiones`
--

CREATE TABLE `camiones` (
  `IdCamion` int(11) NOT NULL,
  `NroCamion` varchar(25) NOT NULL,
  `Marca` varchar(25) NOT NULL,
  `Modelo` varchar(25) NOT NULL,
  `Estado` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `camiones`
--

INSERT INTO `camiones` (`IdCamion`, `NroCamion`, `Marca`, `Modelo`, `Estado`) VALUES
(11, 'Camion 4', 'Mercedes Truck', '2002', 'Mantenimeinto'),
(12, 'Camion 2', 'Renault', 'Kerax 430 DXI', 'Disponible'),
(13, 'Camion 2', 'Renault', 'Kerax 430 DXI', 'Disponible');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `IdCliente` int(11) NOT NULL,
  `NombreCliente` varchar(30) NOT NULL,
  `RUC` varchar(50) NOT NULL,
  `Direccion` varchar(25) NOT NULL,
  `Telefono` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`IdCliente`, `NombreCliente`, `RUC`, `Direccion`, `Telefono`) VALUES
(1, 'Silvio Espinoza', '1336662-9', 'Jose Squeff 522', 971111515),
(2, 'Raquel Insfran', '4179206', 'Rep. Argentina', 981723650),
(3, 'Nicolas Espinoza', '4967183-9', 'Jose Squeff 522', 971875556),
(4, 'Silvio Benjamin Espinoza', '4967185', 'Jose Squeff 522', 971443964);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compras`
--

CREATE TABLE `compras` (
  `IdCompra` int(11) NOT NULL,
  `Proveedor` varchar(50) NOT NULL,
  `DetalleCompra` varchar(100) NOT NULL,
  `DescripCompra` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `compras`
--

INSERT INTO `compras` (`IdCompra`, `Proveedor`, `DetalleCompra`, `DescripCompra`) VALUES
(1, 'Enzo Acuña', 'Bobinas de cable de media tensión - 35000', 'Los necesito en 2 días');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materiales`
--

CREATE TABLE `materiales` (
  `IdMat` int(11) NOT NULL,
  `NombreMaterial` varchar(100) NOT NULL,
  `DescripcionMat` varchar(100) NOT NULL,
  `Precio` int(11) NOT NULL,
  `Cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `materiales`
--

INSERT INTO `materiales` (`IdMat`, `NombreMaterial`, `DescripcionMat`, `Precio`, `Cantidad`) VALUES
(1, 'Bobinas de cable de baja tension', 'Las bobinas son de tamaño mediano', 25000, 100),
(13, 'Bobinas de cable de media tensión', 'Las bobinas son de tamaño grande', 35000, 120),
(15, 'Bobinas de cable de baja tensión', 'Las bobinas son de tamaño pequeño', 7000, 24),
(16, 'Bobinas de cable de baja tensión', 'Las bobinas son de tamaño grande', 39000, 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `IdPedido` int(11) NOT NULL,
  `NombrePro` varchar(50) NOT NULL,
  `DescripPedido` varchar(1000) NOT NULL,
  `FormaPago` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedidos`
--

INSERT INTO `pedidos` (`IdPedido`, `NombrePro`, `DescripPedido`, `FormaPago`) VALUES
(4, 'Facundo Machado', 'Quiero 5 bobinas de cable de media tensión, tamaño mediano', 'Cheque con fecha diferida');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedores`
--

CREATE TABLE `proveedores` (
  `IdPro` int(11) NOT NULL,
  `NombreProveedor` varchar(50) NOT NULL,
  `CIpro` varchar(25) NOT NULL,
  `RUC` varchar(25) NOT NULL,
  `Direccion` varchar(25) NOT NULL,
  `Telefono` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedores`
--

INSERT INTO `proveedores` (`IdPro`, `NombreProveedor`, `CIpro`, `RUC`, `Direccion`, `Telefono`) VALUES
(1, 'Facundo Machado', '1234545', '1234589-9', 'Barrio Santa Clara', 986757776),
(3, 'Enzo Acuña', '23456789', '23456789-1', 'Barrio Santa Helena', 971945812),
(4, 'Fabrizio Machado', '12345678', '12345678-1', 'Barrio Los Jardines', 971675234);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `firstname`, `lastname`, `username`, `password`) VALUES
(1, 'Nicolás', 'Espinoza', 'nico', 'pbkdf2:sha256:600000$12GZ3CF2$a36858a8a1f975e8527c57f57b9494011914ec6b7b13a6e27a468dd268337541'),
(2, 'dani', 'seg', 'daniseg', 'pbkdf2:sha256:600000$1ZRcsoHW$e1db8781835714cd5bd0b283c3c6ff3bd32d4fb3a58a26f4b0324337c629e3da'),
(3, 'Ra', 'quel', 'rq', 'pbkdf2:sha256:600000$Vrabv5mI$c1805fa7a474949a1a4e3668a34121d634d142d46470dd29866ac77c571ad45e'),
(4, 'a', 's', 'as', 'pbkdf2:sha256:600000$jK4SnC0g$1affc05511b62a51ab96ac5abc9675aee420383bd27840e98ec2c5fd17382e29');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `camiones`
--
ALTER TABLE `camiones`
  ADD PRIMARY KEY (`IdCamion`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`IdCliente`);

--
-- Indices de la tabla `compras`
--
ALTER TABLE `compras`
  ADD PRIMARY KEY (`IdCompra`);

--
-- Indices de la tabla `materiales`
--
ALTER TABLE `materiales`
  ADD PRIMARY KEY (`IdMat`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`IdPedido`);

--
-- Indices de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  ADD PRIMARY KEY (`IdPro`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `camiones`
--
ALTER TABLE `camiones`
  MODIFY `IdCamion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `IdCliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT de la tabla `compras`
--
ALTER TABLE `compras`
  MODIFY `IdCompra` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `materiales`
--
ALTER TABLE `materiales`
  MODIFY `IdMat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `IdPedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  MODIFY `IdPro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
