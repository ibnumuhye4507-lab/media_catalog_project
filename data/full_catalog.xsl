<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
        <head>
            <title>ኢስላማዊ ሚዲያ ካታሎግ</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f0f4f0;
                    margin: 0;
                    padding: 40px;
                    direction: ltr;
                }
                .container {
                    max-width: 950px;
                    margin: auto;
                    background: white;
                    padding: 30px;
                    border-radius: 20px;
                    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
                }
                h2 {
                    color: #1b5e20;
                    text-align: center;
                    border-bottom: 4px solid #2e7d32;
                    padding-bottom: 15px;
                    font-size: 28px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 30px;
                }
                th {
                    background-color: #2e7d32;
                    color: white;
                    padding: 18px;
                    text-align: left;
                    font-size: 18px;
                }
                td {
                    padding: 18px;
                    border-bottom: 1px solid #eee;
                    font-size: 16px;
                }
                tr:hover {
                    background-color: #f1f8f1;
                }
                .btn-view {
                    color: white;
                    padding: 10px 20px;
                    text-decoration: none;
                    border-radius: 8px;
                    font-size: 14px;
                    font-weight: bold;
                    display: inline-block;
                }
                .btn-book { background-color: #3498db; }
                .btn-movie { background-color: #2e7d32; }
                
                .type-tag {
                    font-size: 12px;
                    background: #e8f5e9;
                    color: #2e7d32;
                    padding: 4px 10px;
                    border-radius: 12px;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>የኢስላማዊ ሚዲያ ዳሽቦርድ</h2>
                <table>
                    <tr>
                        <th>ዓይነት</th>
                        <th>ርዕስ</th>
                        <th>የወጣበት ዓ.ም</th>
                        <th>ተግባር</th>
                    </tr>
                    <xsl:for-each select="catalog/*">
                    <tr>
                        <td>
                            <span class="type-tag">
                                <xsl:choose>
                                    <xsl:when test="name()='book'">መጽሐፍ</xsl:when>
                                    <xsl:otherwise>ቪዲዮ</xsl:otherwise>
                                </xsl:choose>
                            </span>
                        </td>
                        <td style="font-weight:bold;"><xsl:value-of select="title"/></td>
                        <td><xsl:value-of select="year"/></td>
                        <td>
                            <xsl:choose>
                                <xsl:when test="name()='book'">
                                    <a class="btn-view btn-book" target="_blank">
                                        <xsl:attribute name="href">
                                            <xsl:value-of select="concat('https://www.google.com/search?tbm=bks&amp;q=', title)"/>
                                        </xsl:attribute>
                                        📖 መጽሐፉን አንብብ
                                    </a>
                                </xsl:when>
                                <xsl:otherwise>
                                    <a class="btn-view btn-movie" target="_blank">
                                        <xsl:attribute name="href">
                                            <xsl:value-of select="concat('https://www.youtube.com/results?search_query=', title)"/>
                                        </xsl:attribute>
                                        ▶ ቪዲዮውን እይ
                                    </a>
                                </xsl:otherwise>
                            </xsl:choose>
                        </td>
                    </tr>
                    </xsl:for-each>
                </table>
            </div>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>