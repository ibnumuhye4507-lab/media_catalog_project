<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
        <head>
            <title>የሚዲያ ካታሎግ ሪፖርት</title>
            <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f4f7f6;
        margin: 0;
        padding: 20px;
    }
    .container {
        max-width: 1000px;
        margin: auto;
        background: white;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    h2 {
        color: #2c3e50;
        text-align: center;
        border-bottom: 2px solid #3498db;
        padding-bottom: 10px;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
    }
    th {
        background-color: #3498db;
        color: white;
        padding: 12px;
        text-align: left;
    }
    td {
        padding: 12px;
        border-bottom: 1px solid #ddd;
    }
    tr:hover {
        background-color: #f1f1f1;
    }
    .type-badge {
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 0.8em;
        font-weight: bold;
        text-transform: uppercase;
    }
    .book { background-color: #e8f4fd; color: #3498db; }
    .movie { background-color: #fef9e7; color: #f1c40f; }
</style>
        </head>
        <body>
            <h2>የእኔ ሚዲያ ካታሎግ</h2>
            <table>
                <tr>
                    <th>ዓይነት</th>
                    <th>ርዕስ</th>
                    <th>ዓ.ም</th>
                </tr>
                <xsl:for-each select="catalog/*">
                    <tr>
                        <td><xsl:value-of select="name()"/></td>
                        <td><xsl:value-of select="title"/></td>
                        <td><xsl:value-of select="year"/></td>
                    </tr>
                </xsl:for-each>
            </table>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>