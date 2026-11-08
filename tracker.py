# Sales Sample Inventory & Reorder Tracker

class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity, reorder_threshold):
        self.inventory[item_name] = {
            'quantity': quantity,
            'reorder_threshold': reorder_threshold
        }

    def check_reorder_alerts(self):
        alerts = []
        for item, data in self.inventory.items():
            if data['quantity'] <= data['reorder_threshold']:
                alerts.append(f"ALERT: {item} stock low ({data['quantity']} remaining, threshold: {data['reorder_threshold']})")
        return alerts

if __name__ == "__main__":
    tracker = InventoryTracker()
    tracker.add_item("Waterproofing Membrane Sample", 5, 10)
    tracker.add_item("Sealant Tube Sample", 25, 15)
    
    for alert in tracker.check_reorder_alerts():
        print(alert)
