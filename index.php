<?php
$json_data = file_get_contents('data.json');

if ($json_data === false) {
    die('Error reading JSON file');
}

$data = json_decode($json_data, true);

if (json_last_error() !== JSON_ERROR_NONE) {
    die('Error parsing JSON: ' . json_last_error_msg());
}

if (!is_array($data)) {
    die('Invalid JSON format');
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Gestor de Tareas del Restaurante</title>
    <link rel="stylesheet" href="https://unpkg.com/98.css">
    <style>
        body {
            margin: 32px;
            font-family: sans-serif;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .window {
            width: 80%;
            margin: 20px 0;
        }
        .task-table {
            width: 100%;
            border-collapse: collapse;
        }
        .task-table th, .task-table td {
            border: 1px solid #000;
            padding: 8px;
            text-align: left;
        }
        .task-table th {
            background-color: #e0e0e0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="window">
            <div class="title-bar">
                <div class="title-bar-text">Gestor de Tareas del Restaurante</div>
            </div>
            <div class="window-body">
                <table class="task-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Título</th>
                            <th>Descripción</th>
                            <th>Estado</th>
                            <th>Turno</th>
                            <th>Asignado a</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php foreach ($data as $task): ?>
                            <tr>
                                <td><?php echo htmlspecialchars($task['id']); ?></td>
                                <td><?php echo htmlspecialchars($task['title']); ?></td>
                                <td><?php echo htmlspecialchars($task['description']); ?></td>
                                <td><?php echo htmlspecialchars($task['status']); ?></td>
                                <td><?php echo htmlspecialchars($task['shift']); ?></td>
                                <td><?php echo htmlspecialchars($task['assigned_to']); ?></td>
                            </tr>
                        <?php endforeach; ?>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>
</html>
