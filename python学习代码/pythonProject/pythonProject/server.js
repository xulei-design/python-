const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3006;

// 中间件
app.use(bodyParser.json());
app.use(cors());
app.use(express.static('public'));

// 数据库连接
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'XU938374',
    database: 'dbtest'
});

db.connect((err) => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
        return;
    }
    console.log('MySQL connected...');
});

// 获取所有表格名称的API
app.get('/api/tables', (req, res) => {
    const query = 'SHOW TABLES';
    db.query(query, (err, results) => {
        if (err) {
            return res.status(500).send(err);
        }
        const tables = results.map(row => Object.values(row)[0]);
        res.json(tables);
    });
});

// 根据表格名称获取数据的API
app.get('/api/data/:tableName', (req, res) => {
    const tableName = req.params.tableName;
    const page = parseInt(req.query.page, 10) || 1;
    const limit = parseInt(req.query.limit, 10) || 10;
    const offset = (page - 1) * limit;

    const queryTotal = `SELECT COUNT(*) AS total FROM ??`;
    const queryData = `SELECT * FROM ?? LIMIT ? OFFSET ?`;
    const queryAllData = `SELECT * FROM ??`;

    db.query(queryTotal, [tableName], (err, totalResults) => {
        if (err) {
            return res.status(500).send(err);
        }
        const total = totalResults[0].total;

        db.query(queryData, [tableName, limit, offset], (err, results) => {
            if (err) {
                return res.status(500).send(err);
            }

            db.query(queryAllData, [tableName], (err, allDataResults) => {
                if (err) {
                    return res.status(500).send(err);
                }

                res.json({ total, results, allData: allDataResults });
            });
        });
    });
});

// 启动服务器
app.listen(port, () => console.log(`Server running on port ${port}`));
