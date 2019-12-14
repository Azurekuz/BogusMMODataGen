BEGIN TRANSACTION;
	READ("regions.sql");
	READ("servers.sql");
	READ("users.sql");
	READ("items.sql");
	READ("expansions.sql");
	READ("locations.sql");
	READ("npcs.sql");
COMMIT;