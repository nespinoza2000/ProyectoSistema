-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-01-2024 a las 18:58:26
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
-- Estructura de tabla para la tabla `auditoria`
--

CREATE TABLE `auditoria` (
  `idAuditoria` int(11) NOT NULL,
  `nombreCliente` varchar(255) DEFAULT NULL,
  `accion` varchar(50) NOT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auditoria`
--

INSERT INTO `auditoria` (`idAuditoria`, `nombreCliente`, `accion`, `fecha`) VALUES
(25, 'r Ayala', 'editar', '2024-01-23 17:00:37'),
(26, 'Raquel Morelia Ayala', 'editar', '2024-01-23 17:03:16'),
(27, 'borrar', 'insertar', '2024-01-23 17:12:18'),
(28, 'Borrar', 'editar', '2024-01-23 17:12:44'),
(29, 'a', 'insertar', '2024-01-23 17:14:47'),
(30, 'aB', 'editar', '2024-01-23 17:15:01'),
(31, '62', 'borrar', '2024-01-23 17:15:58'),
(32, 'borrador', 'insertar', '2024-01-23 17:17:34'),
(33, 'Borrada', 'editar', '2024-01-23 17:18:04'),
(34, 'Borarar', 'insertar', '2024-01-23 17:20:39'),
(35, 'Borrar', 'editar', '2024-01-23 17:20:52'),
(36, 'Ramon Espinoza', 'insertar', '2024-01-23 17:22:56'),
(37, 'Morelia Segovia', 'editar', '2024-01-23 17:23:49'),
(38, 'a', 'insertar', '2024-01-23 17:25:30'),
(39, 'aqw', 'editar', '2024-01-23 17:25:48'),
(44, 'Raquel Espinoza', 'editar', '2024-01-23 17:49:10'),
(45, 'Nicolas Espinoza', 'editar', '2024-01-23 17:49:35'),
(46, 'Borrar', 'insertar', '2024-01-23 17:52:53'),
(47, 'Borrar', 'eliminar', '2024-01-23 17:53:28');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `camiones`
--

CREATE TABLE `camiones` (
  `IdCamion` int(11) NOT NULL,
  `NroCamion` varchar(25) NOT NULL,
  `Marca` varchar(25) NOT NULL,
  `Modelo` varchar(25) NOT NULL,
  `Chasis` varchar(50) NOT NULL,
  `Chapa` varchar(50) NOT NULL,
  `Estado` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `camiones`
--

INSERT INTO `camiones` (`IdCamion`, `NroCamion`, `Marca`, `Modelo`, `Chasis`, `Chapa`, `Estado`) VALUES
(14, '1', 'Scania', 'Kerax 430 DXI', 'KQL900XXXXA', 'NBC 632', 'Disponible');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `IdCliente` int(11) NOT NULL,
  `NombreCliente` varchar(30) NOT NULL,
  `RUC` varchar(50) NOT NULL,
  `Direccion` varchar(25) NOT NULL,
  `Domicilio` varchar(50) NOT NULL,
  `Telefono` int(11) NOT NULL,
  `Email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`IdCliente`, `NombreCliente`, `RUC`, `Direccion`, `Domicilio`, `Telefono`, `Email`) VALUES
(1, 'SR Espinoza', '1336662-9', 'Jose Squeff 522', 'Barrio Buena Vista', 971111515, 'srec69@gmail.com'),
(2, 'Raquel Insfran', '4179206', 'Rep. Argentina', 'Barrio Buena Vista', 981723650, 'RaqueInsfran18@gmail.com'),
(3, 'Nicolas Espinoza', '4967183-9', 'José Squeff', 'Barrio Buena Vista', 971875556, 'nespinozasegovia@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compras`
--

CREATE TABLE `compras` (
  `IdCompra` int(11) NOT NULL,
  `Proveedor` varchar(50) NOT NULL,
  `Material` varchar(100) NOT NULL,
  `Descripcion` varchar(100) NOT NULL,
  `Detalle` varchar(100) NOT NULL,
  `Pago` varchar(65) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `compras`
--

INSERT INTO `compras` (`IdCompra`, `Proveedor`, `Material`, `Descripcion`, `Detalle`, `Pago`) VALUES
(4, 'Fabrizio Machado', 'Bobina de cable de media tension', 'Tamaño mediano ', 'Pago inmediato', 'Transferencia bancaria');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `financiera`
--

CREATE TABLE `financiera` (
  `IdFinanza` int(11) NOT NULL,
  `Capital` int(11) NOT NULL,
  `Activo` int(11) NOT NULL,
  `Pasivo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `financiera`
--

INSERT INTO `financiera` (`IdFinanza`, `Capital`, `Activo`, `Pasivo`) VALUES
(10, 90000000, 1225000, 750000),
(12, 90000000, 1250000, 500000);

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
(1, 'Bobinas de cable de baja tension', 'tamaño pequeño', 25000, 200),
(13, 'Bobinas de cable de baja tensión', 'tamaño mediano', 35000, 240),
(17, 'Bobina de cable de baja tensión', 'tamaño grande', 45000, 150),
(18, 'Bobina de cable de media tensión', 'tamaño pequeño', 50000, 230),
(19, 'Bobina de cable de media tensión', 'tamaño mediano', 67000, 280),
(20, 'Bobina de cable de media tensión', 'tamaño grande', 87000, 350);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagos`
--

CREATE TABLE `pagos` (
  `IdPago` int(11) NOT NULL,
  `Proveedor` varchar(100) NOT NULL,
  `Actividad` varchar(100) NOT NULL,
  `Monto` int(11) NOT NULL,
  `FormaPago` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pagos`
--

INSERT INTO `pagos` (`IdPago`, `Proveedor`, `Actividad`, `Monto`, `FormaPago`) VALUES
(1, 'Fabrizio Machado', 'Por compra de materiales', 12000000, 'Transferencia bancaria'),
(2, 'Fabrizio Machado', 'Por pedido de materiales', 250000, 'Efectivo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `IdPedido` int(11) NOT NULL,
  `NombrePro` varchar(50) NOT NULL,
  `NombreMat` varchar(50) NOT NULL,
  `Cantidad` int(11) NOT NULL,
  `Caracteristicas` varchar(100) NOT NULL,
  `FormaPago` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedidos`
--

INSERT INTO `pedidos` (`IdPedido`, `NombrePro`, `NombreMat`, `Cantidad`, `Caracteristicas`, `FormaPago`) VALUES
(5, 'Fabrizio Machado', 'Cable de media tensión', 80, 'Bobina de tamaño mediano', 'Transferencia bancaria');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedores`
--

CREATE TABLE `proveedores` (
  `IdPro` int(11) NOT NULL,
  `NombreProveedor` varchar(50) NOT NULL,
  `RUC` varchar(25) NOT NULL,
  `Direccion` varchar(25) NOT NULL,
  `Domicilio` varchar(50) NOT NULL,
  `Telefono` int(11) NOT NULL,
  `Email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedores`
--

INSERT INTO `proveedores` (`IdPro`, `NombreProveedor`, `RUC`, `Direccion`, `Domicilio`, `Telefono`, `Email`) VALUES
(5, 'Fabrizio Machado', '1234514-9', 'Av. Boquerón 789', 'Barrio San Roque', 956123455, 'fabriziomachadoacuna@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `IdRol` int(11) NOT NULL,
  `Descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tareas`
--

CREATE TABLE `tareas` (
  `IdTarea` int(11) NOT NULL,
  `Tarea` varchar(50) NOT NULL,
  `Detalles` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tareas`
--

INSERT INTO `tareas` (`IdTarea`, `Tarea`, `Detalles`) VALUES
(3, 'Gestionar Inventario', 'Verificar la lista de materiales.\r\nActualícela de ser necesario.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `IdRol` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `firstname`, `lastname`, `username`, `password`, `IdRol`) VALUES
(3, 'Daniel', 'Segovia', 'daniseg', 'pbkdf2:sha256:600000$VvsRLnsE$d204396669fd3dfff3ea4c1aed04bf7ffe1a0c229787e68361b828330094f65a', NULL),
(4, 'Nicolás', 'Espinoza', 'nico', 'pbkdf2:sha256:600000$35bMdKgO$36ffc289c6a3ad6550608cb8ef859ddfa5e6cfb7bf7fdf3eb8c6f259c1691f98', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `IdVenta` int(11) NOT NULL,
  `Cliente` varchar(50) NOT NULL,
  `Material` varchar(1000) NOT NULL,
  `Cantidad` varchar(100) NOT NULL,
  `Precio` int(20) NOT NULL,
  `FormaPago` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`IdVenta`, `Cliente`, `Material`, `Cantidad`, `Precio`, `FormaPago`) VALUES
(4, 'Raquel Insfran', 'Bobinas de cable de baja tension', '10', 25000, 'Transferencia bancaria');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auditoria`
--
ALTER TABLE `auditoria`
  ADD PRIMARY KEY (`idAuditoria`);

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
-- Indices de la tabla `financiera`
--
ALTER TABLE `financiera`
  ADD PRIMARY KEY (`IdFinanza`);

--
-- Indices de la tabla `materiales`
--
ALTER TABLE `materiales`
  ADD PRIMARY KEY (`IdMat`);

--
-- Indices de la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD PRIMARY KEY (`IdPago`);

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
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`IdRol`);

--
-- Indices de la tabla `tareas`
--
ALTER TABLE `tareas`
  ADD PRIMARY KEY (`IdTarea`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `fk_users_roles` (`IdRol`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`IdVenta`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auditoria`
--
ALTER TABLE `auditoria`
  MODIFY `idAuditoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT de la tabla `camiones`
--
ALTER TABLE `camiones`
  MODIFY `IdCamion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `IdCliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;

--
-- AUTO_INCREMENT de la tabla `compras`
--
ALTER TABLE `compras`
  MODIFY `IdCompra` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `financiera`
--
ALTER TABLE `financiera`
  MODIFY `IdFinanza` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `materiales`
--
ALTER TABLE `materiales`
  MODIFY `IdMat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `pagos`
--
ALTER TABLE `pagos`
  MODIFY `IdPago` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `IdPedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  MODIFY `IdPro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `IdRol` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tareas`
--
ALTER TABLE `tareas`
  MODIFY `IdTarea` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `IdVenta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `fk_users_roles` FOREIGN KEY (`IdRol`) REFERENCES `roles` (`IdRol`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
