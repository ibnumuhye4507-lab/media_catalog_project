<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
        <head>
            <title>የሚዲያ ካታሎግ ሪፖርት</title>
            <style>
                table { border-collapse: collapse; width: 100%; }
                th, td { border: 1px solid black; padding: 10px; text-align: left; }
                th { background-color: #f2f2f2; }
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