<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<html>
			<head>
				<link rel="stylesheet" type="text/css" href="oyecomova.css"></link>
			</head>
			<body>
				<span>
				<h2>Tito Puente y Celia Cruz presentan : </h2>
				<h1>Oye Como vá<xsl:value-of select="titulo"/></h1>
				<br/>
				</span>
				<xsl:for-each select="cancion/letra/estrofa">
					<xsl:sort select="orden"/>
					<xsl:for-each select="verso">
						<p><xsl:value-of select="."/></p>
					</xsl:for-each>
					<br/>
				</xsl:for-each>
				<p>Autor-Tito Puente<xsl:value-of select="titulo"/></p>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>