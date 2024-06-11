import pytest

from .app import InventreeApp


@pytest.mark.asyncio
async def test_part_search():
    """Test part seach."""
    app = InventreeApp()
    async with app.run_test() as pilot:  
        # Switch to the Part search screen
        await pilot.click("#part-search-tab", control=True)

        # Do empty search
        await pilot.press("enter")

        # Do a search for a part that exists
        await pilot.click("#part_search_input")
        await pilot.press(*"RPI-0001")
        await pilot.press("enter")

        status = app.query_one('#part_search_status_text')
        assert status.renderable.plain == "Status Ok"
